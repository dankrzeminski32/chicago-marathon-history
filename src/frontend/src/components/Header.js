import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import { Link } from "react-router-dom";

function Header({ marathon, isYearSelected, onShow }) {
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
                        <Nav.Link href="">
                            <Link onClick={onShow} to="/">
                                Home
                            </Link>
                        </Nav.Link>
                        <Nav.Link href="">About</Nav.Link>
                        {isYearSelected ? (
                            <Nav.Link
                                onClick={onShow}
                                id="changeYearLink"
                                href=""
                            >
                                Change Year
                            </Nav.Link>
                        ) : null}
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
}

export default Header;
