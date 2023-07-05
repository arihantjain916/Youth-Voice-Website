import About from "../about/About";
import LoginPopup from "../common/form/login/LoginPopup";
import FooterDefault from "../footer/common-footer";
import DefaulHeader2 from "../header/DefaulHeader2";
import FetchBlog from "../blog/BlogFetch";

console.log(FetchBlog);

const index = () => {
  return (
    <>
      <LoginPopup />

      <DefaulHeader2 />
      <section className="news-section">
        <div className="auto-container">
          <div className="sec-title text-center">
            <h2>Recent Blogs</h2>
            <div className="text">Blogs posted each day.</div>
          </div>
          <div className="row" data-aos="fade-up">
            <FetchBlog />
          </div>
        </div>
      </section>
      <section className="about-section">
        <div className="auto-container">
          <div className="row">
            <About />
          </div>
        </div>
      </section>
      <FooterDefault />
    </>
  );
};
export default index;
