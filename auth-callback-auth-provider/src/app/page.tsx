"use client";

import {
  LoginLink,
  LogoutLink,
  useKindeBrowserClient,
} from "@kinde-oss/kinde-auth-nextjs";

export default function Home() {
  const { isAuthenticated } = useKindeBrowserClient();

  return (
    <main className="flex justify-center gap-4 p-24">
      {!isAuthenticated ? (
        <LoginLink className="p-10 text-zinc-900 text-2xl font-semibold rounded-lg bg-zinc-100">
          Log in
        </LoginLink>
      ) : (
        <LogoutLink className="p-10 text-zinc-900 text-2xl font-semibold rounded-lg bg-zinc-100">
          Log out
        </LogoutLink>
      )}
    </main>
  );
}
