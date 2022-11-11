import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import Button from "react-bootstrap/Button";
import ToggleButton from "react-bootstrap/ToggleButton";
import ToggleButtonGroup from "react-bootstrap/ToggleButtonGroup";

function FilterNavbar({ selected, setSelected }) {
    function onChangeValue(event) {
        setSelected(event.target.value);
    }
    return (
        <Navbar className="inner-nav" expand="lg">
            <Container>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <ToggleButtonGroup
                        type="radio"
                        name="options"
                        defaultValue={1}
                        id="inner-button-group"
                        onChange={setSelected}
                        value={selected}
                    >
                        <ToggleButton
                            variant="secondary"
                            id="tbg-radio-1"
                            value={1}
                        >
                            Overview
                        </ToggleButton>
                        <ToggleButton
                            variant="secondary"
                            id="tbg-radio-2"
                            value={2}
                        >
                            Top Finishers
                        </ToggleButton>
                        <ToggleButton
                            variant="secondary"
                            id="tbg-radio-3"
                            value={3}
                        >
                            Participant Data
                        </ToggleButton>
                    </ToggleButtonGroup>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
}

export default FilterNavbar;
