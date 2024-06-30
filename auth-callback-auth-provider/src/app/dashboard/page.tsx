import { db } from "@/db";
import { getKindeServerSession } from "@kinde-oss/kinde-auth-nextjs/server";
import { redirect } from "next/navigation";

const Page = async () => {
  const { getUser } = getKindeServerSession();
  const user = await getUser();

  if (!user?.id) redirect("/api/auth/login");

  const userInDB = await db.user.findUnique({
    where: {
      id: user.id,
    },
  });

  if (!userInDB) redirect("/auth/callback");

  return (
    <div className="flex flex-col justify-center items-center sm:mt-36 w-full mt-20">
      <h1 className="font-semibold text-zinc-900 text-2xl">
        You are authenticated
      </h1>
      <p className="font-medium text-xl text-zinc-700 text-center">
        The user has also been created in the DB
      </p>
    </div>
  );
};

export default Page;
