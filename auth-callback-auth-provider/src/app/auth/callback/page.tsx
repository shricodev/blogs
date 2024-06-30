import { getKindeServerSession } from "@kinde-oss/kinde-auth-nextjs/server";
import { redirect } from "next/navigation";
import { db } from "@/db";

const Page = async () => {
  const { getUser } = getKindeServerSession();
  const user = await getUser();

  if (!user?.id || !user?.email) redirect("/");

  const name =
    user?.given_name && user?.family_name
      ? `${user.given_name} ${user.family_name}`
      : user?.given_name || null;

  const userInDB = await db.user.findFirst({
    where: {
      id: user.id,
    },
  });

  if (!userInDB) {
    await db.user.create({
      data: {
        id: user.id,
        email: user.email,
        ...(name && { name }),
      },
    });
  }

  redirect("/dashboard");
};

export default Page;
