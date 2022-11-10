import Header from "./Header";
import Sidebar from "./Sidebar";
import Container from "react-bootstrap/Container";

function Layout({ children }) {
    return (
        <div className="App">
            <Header></Header>
            <Sidebar></Sidebar>
            <Container>{children}</Container>
        </div>
    );
}
export default Layout;
