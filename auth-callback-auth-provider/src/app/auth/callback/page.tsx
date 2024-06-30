import { Loader2 } from "lucide-react";
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

  if (userInDB) redirect("/dashboard");

  if (!userInDB) {
    await db.user.create({
      data: {
        id: user.id,
        email: user.email,
        ...(name && { name }),
      },
    });

    redirect("/dashboard");
  }

  return (
    <div className="mt-20 flex w-full items-center justify-center sm:mt-36">
      <div className="flex flex-col items-center gap-2">
        <Loader2 className="h-8 w-8 animate-spin text-primary" />
        <h3 className="text-center text-xl font-semibold">
          Setting up your account. Please hold tight... 🫡
        </h3>
        <p className="text-center">You will be redirected automatically.</p>
      </div>
    </div>
  );
};

export default Page;
