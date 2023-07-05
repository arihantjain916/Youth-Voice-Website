import Link from "next/link";
const HeaderNavContent = () => {
  return (
    <>
      <nav className="nav main-menu">
        <li></li>
        <ul className="navigation" id="navbar">
          <div className="mega-menu">
            <div className="mega-menu-bar row pt-0">
              <Link href="/blog">Blog</Link>
            </div>
          </div>
        </ul>
      </nav>
    </>
  );
};

export default HeaderNavContent;
