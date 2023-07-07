import { useState } from "react";

const ContactForm = () => {
  const [email, setEmail] = useState("");
  const [name, setName] = useState("");
  const [message, setMessage] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [successMessage, setSuccessMessage] = useState("");
  const [showAlert, setShowAlert] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const data = {
      email: email,
      name: name,
      message: message,
    };

    if (name.length < 3 || message.length < 5) {
      let errors = [];
      if (name.length < 3) {
        errors.push("Name must contain a minimum of three characters.");
      }
      if (message.length < 5) {
        errors.push("Message should be more than 5 characters long.");
      }
      setErrorMessage(errors.join(" "));
    } else {
      try {
        const response = await fetch("http://127.0.0.1:8000/contact-us/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
        });

        let success = [];
        let errors = [];
        if (response.ok) {
          success.push("Message Sent Successfully");
          setShowAlert(true);
          setEmail("");
          setName("");
          setMessage("");
        } else {
          errors.push("Failed to send the message. Please try again later.");
        }
        setErrorMessage(errors);
        setSuccessMessage(success.join(" "));
      } catch (error) {
        console.log("Error:", error);
      }
    }
  };

  return (
    <>
      <section className="contact-section">
        <div className="contact-form default-form">
          {showAlert && (
            <div
              className="alert alert-success d-flex align-items-center"
              role="alert"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                className="bi bi-check2-all"
                viewBox="0 0 16 16"
              >
                <path d="M12.354 4.354a.5.5 0 0 0-.708-.708L5 10.293 1.854 7.146a.5.5 0 1 0-.708.708l3.5 3.5a.5.5 0 0 0 .708 0l7-7zm-4.208 7-.896-.897.707-.707.543.543 6.646-6.647a.5.5 0 0 1 .708.708l-7 7a.5.5 0 0 1-.708 0z" />
                <path d="m5.354 7.146.896.897-.707.707-.897-.896a.5.5 0 1 1 .708-.708z" />
              </svg>
              <div>{successMessage}</div>
            </div>
          )}
          <h3>Leave A Message</h3>

          <form onSubmit={handleSubmit}>
            <div className="row">
              <div className="form-group col-lg-12 col-md-12 col-sm-12">
                <div className="response">{errorMessage}</div>
              </div>

              <div className="col-lg-6 col-md-12 col-sm-12 form-group">
                <label>Your Name</label>
                <input
                  type="text"
                  name="name"
                  className="name"
                  placeholder="Your Name"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  required
                />
              </div>

              <div className="col-lg-6 col-md-12 col-sm-12 form-group">
                <label>Your Email</label>
                <input
                  type="email"
                  name="email"
                  className="email"
                  placeholder="Your Email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                />
              </div>

              <div className="col-lg-12 col-md-12 col-sm-12 form-group">
                <label>Your Message</label>
                <textarea
                  name="message"
                  placeholder="Write your message..."
                  value={message}
                  onChange={(e) => setMessage(e.target.value)}
                  required
                ></textarea>
              </div>

              <div className="col-lg-12 col-md-12col-sm-12 form-group">
                <button
                  className="theme-btn btn-style-one"
                  type="submit"
                  id="submit"
                  name="submit-form"
                >
                  Send Message
                </button>
              </div>
            </div>
          </form>
        </div>
      </section>
    </>
  );
};

export default ContactForm;
