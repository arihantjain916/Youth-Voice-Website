import Link from "next/link";
import LoginPopup from "../../components/common/form/login/LoginPopup";
import FooterDefault from "../../components/footer/common-footer";
import DefaulHeader from "../../components/header/DefaulHeader2";
import Contact from "../../components/pages-menu/contact/ContactForm";

export const getStaticProps = async () => {
  const res = await fetch("http://127.0.0.1:8000/api/details/blogs/");
  const data = await res.json();

  return {
    props: {
      data: data,
    },
    revalidate: 20,
  };
};

const blog = ({ data }) => {
  return (
    <>
      <span className="header-span"></span>

      <LoginPopup />

      <DefaulHeader />
      {data?.map((data) => {
        return (
          <div
            className="news-block-two col-lg-6 col-md-6 col-sm-12"
            key={data.id}
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
                <Link href={`/blog/${data.slug}`}>{data.title}</Link>
              </h3>
              <p className="text">{data.content}</p>
              <Link href={`/blog/${data.slug}`} className="read-more">
                Read More <i className="fa fa-angle-right"></i>
              </Link>
            </div>
          </div>
        );
      })}
      <Contact />
      <FooterDefault footerStyle="alternate5" />
    </>
  );
};

export const threeblog = () => {
  return (
    <>
      {data.slice(0, 3).map((data) => {
        return (
          <div
            className="news-block-two col-lg-6 col-md-6 col-sm-12"
            key={data.id}
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
                <Link href={`/blog/${data.slug}`}>{data.title}</Link>
              </h3>
              <p className="text">{data.content}</p>
              <Link href={`/blog/${data.slug}`} className="read-more">
                Read More <i className="fa fa-angle-right"></i>
              </Link>
            </div>
          </div>
        );
      })}
    </>
  );
};

export default blog;
// threeblog;
