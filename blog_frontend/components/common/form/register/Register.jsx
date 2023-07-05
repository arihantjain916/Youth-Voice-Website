import { Tabs } from "react-tabs";
import LoginWithSocial from "./LoginWithSocial";
import Form from "./FormContent";

const Register = () => {
  return (
    <div className="form-inner">
      <h3>Create a Free Account</h3>

      <Tabs>
        <div className="form-group register-dual">
          <Form />
        </div>
      </Tabs>
      {/* End form-group */}

      <div className="bottom-box">
        <div className="divider">
          <span>or</span>
        </div>
        <LoginWithSocial />
      </div>
      {/* End bottom-box LoginWithSocial */}
    </div>
  );
};

export default Register;
