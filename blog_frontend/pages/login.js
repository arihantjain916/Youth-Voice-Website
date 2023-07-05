import dynamic from "next/dynamic";
import Seo from "../components/common/Seo";
import LogIn from "../components/pages-menu/login";
// import LogIn from "../components/common/form/login/LoginPopup"

const index = () => {
  return (
    <>
      <Seo pageTitle="Login" />
      <LogIn />
    </>
  );
};

export default dynamic(() => Promise.resolve(index), { ssr: false });
