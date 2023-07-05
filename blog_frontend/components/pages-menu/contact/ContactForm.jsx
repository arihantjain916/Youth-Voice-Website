import { useState } from "react";
const ContactForm = () => {
  const [email, setEmail] = useState("");
  const [name, setName] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const data = {
      email: email,
      name: name,
      message: message,
    };

    try {
      const response = await fetch("http://127.0.0.1:8000/contact-us/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        // const data = await response.JSON(),
        body: JSON.stringify(data),
      });

      if (response.ok) {
        console.log("Message Sent!");
      }
      else{
        alert('Message should have atleast 5 letters and Name have atleast 3 letters') ;
      }
    } catch (error) {
      console.log("Error:", error);
    }
  };
  return (
    <>
      <section className="contact-section">
        <div className="contact-form default-form">
          <h3>Leave A Message</h3>

          <form onSubmit={handleSubmit}>
            <div className="row">
              <div className="form-group col-lg-12 col-md-12 col-sm-12">
                <div className="response"></div>
              </div>
              {/* End .col */}

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
              {/* End .col */}

              <div className="col-lg-12 col-md-12 col-sm-12 form-group">
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
