import LoginPopup from "../../common/form/login/LoginPopup";
import FooterDefault from "../../footer/common-footer";
import ContactForm from "./ContactForm";
import DefaulHeader from "../../header/DefaulHeader2";

const index = () => {
  return (
    <>
      <section className="contact-section">
        <LoginPopup />

        <DefaulHeader />

        <div className="contact-form default-form">
          <ContactForm />
          {/* <!--Contact Form--> */}
        </div>
        {/* <!--End Contact Form --> */}
      </section>
      {/* <!-- Contact Section --> */}

      <FooterDefault footerStyle="alternate5" />
      {/* <!-- End Main Footer --> */}
    </>
  );
};

export default index;
