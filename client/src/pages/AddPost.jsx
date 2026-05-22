function AddPost() {
  return (
    <section className="max-w-2xl">
      <h1 className="text-3xl font-bold text-slate-950">Add Post</h1>

      <form className="mt-6 space-y-4 rounded-lg border border-slate-200 bg-white p-6">
        <div>
          <label htmlFor="title" className="block text-sm font-medium text-slate-700">
            Title
          </label>
          <input
            id="title"
            type="text"
            className="mt-2 w-full rounded-md border border-slate-300 px-3 py-2 outline-none focus:border-slate-900 focus:ring-2 focus:ring-slate-200"
            placeholder="Post title"
          />
        </div>

        <div>
          <label htmlFor="content" className="block text-sm font-medium text-slate-700">
            Content
          </label>
          <textarea
            id="content"
            rows="6"
            className="mt-2 w-full rounded-md border border-slate-300 px-3 py-2 outline-none focus:border-slate-900 focus:ring-2 focus:ring-slate-200"
            placeholder="Write your post"
          />
        </div>

        <button
          type="submit"
          className="rounded-md bg-slate-900 px-4 py-2 text-sm font-semibold text-white hover:bg-slate-700"
        >
          Create post
        </button>
      </form>
    </section>
  );
}

export default AddPost;
