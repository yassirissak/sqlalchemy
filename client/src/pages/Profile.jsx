function Profile() {
  return (
    <section className="space-y-6">
      <h1 className="text-3xl font-bold text-slate-950">Profile</h1>

      <div className="rounded-lg border border-slate-200 bg-white p-6">
        <div className="flex flex-col gap-4 sm:flex-row sm:items-center">
          <div className="flex h-20 w-20 items-center justify-center rounded-full bg-slate-200 text-2xl font-bold text-slate-600">
            JD
          </div>
          <div>
            <h2 className="text-xl font-semibold text-slate-950">John Doe</h2>
            <p className="text-slate-600">john@example.com</p>
            <p className="mt-1 text-sm text-slate-500">@johndoe</p>
          </div>
        </div>
      </div>
    </section>
  );
}

export default Profile;
