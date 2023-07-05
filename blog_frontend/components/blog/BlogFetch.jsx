// import Link from "next/link";
// import { useEffect, useState } from "react";
// import axios from "axios";
// // export const getStaticProps = async () => {
// //   try {
// //     const res = await fetch("http://127.0.0.1:8000/api/details/blogs/");
// //     const data = await res.json();
// //     console.log(res);

// //     if (res.ok) {
// //       console.log(data);
// //     } else {
// //       console.log("error");
// //     }

// //     return {
// //       props: {
// //         data: data,
// //       },
// //     };
// //   } catch (error) {
// //     console.error("Error fetching data:", error);
// //     return {
// //       props: {
// //         data: [],
// //       },
// //     };
// //   }
// // };

// const FetchBlog = () => {
//   try {
//     let response = axios
//       .get("http://127.0.0.1:8000/api/details/blogs/")
//       .then((response) => {
//         const data = response.data;
//         console.log(data);
//         if (!Array.isArray(data))
//           return (
//             <>
//               <h1>No data found</h1>
//             </>
//           );
//         else {
//           return (
//             <>
//               {data.slice(0, 3).map((data) => {
//                 return (
//                   <div
//                     className="news-block-two col-lg-6 col-md-6 col-sm-12"
//                     key={data.id}
//                   >
//                     <div className="content-box">
//                       <ul className="post-meta">
//                         <li>
//                           <a href="#">July 04, 23</a>
//                         </li>
//                         <li>
//                           <a href="#">12 Comment</a>
//                         </li>
//                       </ul>
//                       <h3>
//                         <Link href={`/blog/${data.slug}`}>{data.title}</Link>
//                       </h3>
//                       <p className="text">{data.content}</p>
//                       <Link href={`/blog/${data.slug}`} className="read-more">
//                         Read More <i className="fa fa-angle-right"></i>
//                       </Link>
//                     </div>
//                   </div>
//                 );
//               })}
//             </>
//           );
//         }
//       });
//   } catch (err) {
//     throw err;
//   }
// };
// FetchBlog();

// // // fetchapi();

// // const Blog = ({ data }) => {
// //   // const { blog } = data
// //   console.log(data);
// //   return (
// //     <>
// //       {data?.slice(0, 3).map((data) => {
// //         return (
// //           <div
// //             className="news-block-two col-lg-6 col-md-6 col-sm-12"
// //             key={data.id}
// //           >
// //             <div className="content-box">
// //               <ul className="post-meta">
// //                 <li>
// //                   <a href="#">July 04, 23</a>
// //                 </li>
// //                 <li>
// //                   <a href="#">12 Comment</a>
// //                 </li>
// //               </ul>
// //               <h3>
// //                 <Link href={`/blog/${data.slug}`}>{data.title}</Link>
// //               </h3>
// //               <p className="text">{data.content}</p>
// //               <Link href={`/blog/${data.slug}`} className="read-more">
// //                 Read More <i className="fa fa-angle-right"></i>
// //               </Link>
// //             </div>
// //           </div>
// //         );
// //       })}
// //     </>
// //   );
// // };

// export default FetchBlog;
// // Now the getStaticProps function properly returns the props object with the fetched data, and the Blog component can use it as intended. Additionally, I've added a try-catch block to handle any potential errors that may occur during the data fetching process.

import Link from "next/link";
import { useEffect, useState } from "react";
import axios from "axios";

const FetchBlog = () => {
  const [blogs, setBlogs] = useState([]);

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
        blogs.map((blog) => (
          <div
            className="news-block-two col-lg-6 col-md-6 col-sm-12"
            key={blog.id}
          >
            <div className="content-box">
              <ul className="post-meta">
                <li>
                  <a href="#">July 04, 23</a>
                </li>
                <li>
                  <a href="#">12 Comment</a>
                </li>
              </ul>
              <h3>
                <Link href={`/blog/${blog.slug}`}>{blog.title}</Link>
              </h3>
              <p className="text">{blog.content}</p>
              <Link href={`/blog/${blog.slug}`} className="read-more">
                Read More <i className="fa fa-angle-right"></i>
              </Link>
            </div>
          </div>
        ))
      )}
    </>
  );
};

export default FetchBlog;
