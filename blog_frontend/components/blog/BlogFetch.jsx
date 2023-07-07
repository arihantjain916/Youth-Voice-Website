import { useEffect, useState } from "react";
import axios from "axios";
import { useRouter } from "next/router";

const FetchBlog = () => {
  const [blogs, setBlogs] = useState([]);
  const router = useRouter();

  useEffect(() => {
    const fetchBlogs = async () => {
      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/api/details/blogs/"
        );
        const data = response.data;

        if (Array.isArray(data)) {
          setBlogs(data.slice(0, 3));
        }
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchBlogs();
  }, []);

  return (
    <>
      {blogs.length === 0 ? (
        <h1>No data found</h1>
      ) : (
        <div className="container mx-auto">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {blogs.map((blog) => (
              <div key={blog.id} className="bg-gray-100 p-4 rounded-lg">
                <h1 className="text-2xl font-medium mb-4">{blog.title}</h1>
                <p className="mb-4">{blog.content.slice(0, 250)}</p>
                <a
                  href={`/blog/${blog.slug}`}
                  onClick={(e) => {
                    e.preventDefault();
                    router.push(`/blog/${blog.slug}`);
                  }}
                  className="text-indigo-500 inline-flex items-center"
                >
                  Learn More
                  <svg
                    className="w-4 h-4 ml-2"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    strokeWidth="2"
                    fill="none"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  >
                    <path d="M5 12h14"></path>
                    <path d="M12 5l7 7-7 7"></path>
                  </svg>
                </a>
              </div>
            ))}
          </div>
        </div>
      )}
    </>
  );
};

export default FetchBlog;
