import dynamic from "next/dynamic";
import Seo from "../components/common/Seo";
import Home1 from "../components/home-1";
// import AuthContext from "../api/AuthContext";

const index = () => {
    return (
        <>
            <Seo pageTitle="Home-1" />
            <Home1 />
            {/* <AuthContext /> */}
        </>
    );
};

export default dynamic(() => Promise.resolve(index), { ssr: false });
