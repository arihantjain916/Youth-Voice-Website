import LoginPopup from "../../common/form/login/LoginPopup";
import FooterDefault from "../../footer/common-footer";
import DefaulHeader from "../../header/DefaulHeader2";
import IntroDescriptions from "./IntroDescriptions";


const index = () => {
  return (
    <>
      {/* <!-- Header Span --> */}
      <span className="header-span"></span>

      <LoginPopup />
      {/* End Login Popup Modal */}

      <DefaulHeader />
      {/* <!--End Main Header --> */}

      {/* <MobileMenu /> */}
      {/* End MobileMenu */}

      {/* <Breadcrumb title="About Us" meta="About Us" /> */}
      {/* <!--End Page Title--> */}

      <section className="about-section-three">
        <div className="auto-container">
          <IntroDescriptions />
        </div>
      </section>

      <FooterDefault />
      {/* <!-- End Main Footer --> */}
    </>
  );
};

export default index;
