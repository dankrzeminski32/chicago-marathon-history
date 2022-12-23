import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import { Link } from "react-router-dom";

function Header({ marathon }) {
    return (
        <Navbar className="main-header-bar" bg="light" expand="lg">
            <Container>
                <Navbar.Brand>
                    Chicago Marathon History{" "}
                    {marathon && <strong>- {marathon.year}</strong>}
                </Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto">
                        <Nav.Link href="#home">
                            <Link to="/">Home</Link>
                        </Nav.Link>
                        <Nav.Link href="#link">About</Nav.Link>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
}

export default Header;
