import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import { Link } from "react-router-dom";

function Header({ marathon, isYearSelected, onShow, onGoHome }) {
    return (
        <Navbar
            collapseOnSelect
            className="main-header-bar"
            bg="light"
            expand="md"
        >
            <Container fluid>
                <Navbar.Brand className>
                    Chicago Marathon History{" "}
                    {marathon && <strong>- {marathon.year}</strong>}
                </Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto">
                        <Nav.Link eventKey="1" href="">
                            <Link onClick={onGoHome} to="/">
                                Home
                            </Link>
                        </Nav.Link>
                        <Nav.Link eventKey="2" href="">
                            About
                        </Nav.Link>
                        <Nav.Link
                            eventKey="3"
                            onClick={onShow}
                            id="changeYearLink"
                            href=""
                            className="d-block d-md-none"
                        >
                            {isYearSelected ? "Change Year" : "Select Year"}
                        </Nav.Link>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
}

export default Header;
