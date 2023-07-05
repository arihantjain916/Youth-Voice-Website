import LoginPopup from "../../components/common/form/login/LoginPopup";
import FooterDefault from "../../components/footer/common-footer";
import DefaulHeader from "../../components/header/DefaulHeader2";
import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import Seo from "../../components/common/Seo";
import Contact from "../../components/pages-menu/contact/ContactForm";

const BlogDetails = ({ conten }) => {
  // const [plaintext, setPlainText] = useState("");
  const router = useRouter();
  const { slug } = router.query;
  const [blog, setBlog] = useState(null);

  useEffect(() => {
    // const parser = new DOMParser();
    // const doc = parser.parseFromString(conten, "text/html");
    // const text = doc.body.textContent || "";
    // setPlainText(text);
    const fetchBlogDetails = async () => {
      try {
        const res = await fetch(
          `http://127.0.0.1:8000/api/details/blogs/${slug}/`
        );
        const data = await res.json();
        setBlog(data);
      } catch (error) {
        console.error("Error fetching blog details:", error);
      }
    };

    if (slug) {
      fetchBlogDetails();
    }
  }, [slug]);

  return (
    <>
      <Seo pageslug="Blog Details " />

      {/* <!-- Header Span --> */}
      <span className="header-span"></span>

      <LoginPopup />
      {/* End Login Popup Modal */}

      <DefaulHeader />
      {/* <!-- End Blog Single --> */}

      <div>
        {blog ? (
          <section className="blog-single">
            <div className="auto-container">
              <div className="upper-box">
                <h3>{blog?.title}</h3>

                <ul className="post-info">
                  <li>August 31, 2021</li>
                  <li>12 Comment</li>
                </ul>
                <h2>{blog.content}</h2>
              </div>
            </div>
          </section>
        ) : (
          <h1>No Blogs Found</h1>
        )}
      </div>
      <a href="/blog">
        <button className="theme-btn btn-style-one" type="submit" name="log-in">
          Back
        </button>
      </a>
      <Contact />
      <FooterDefault footerStyle="alternate5" />
      {/* <!-- End Main Footer --> */}
    </>
  );
};

export default BlogDetails;
