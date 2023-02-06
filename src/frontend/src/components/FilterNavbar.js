import Container from "react-bootstrap/Container";
import Navbar from "react-bootstrap/Navbar";
import ToggleButton from "react-bootstrap/ToggleButton";
import ToggleButtonGroup from "react-bootstrap/ToggleButtonGroup";

function FilterNavbar({ selected, setSelected }) {
    return (
        <Navbar className="inner-nav">
            <Container>
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
                        Top Finishers - Male
                    </ToggleButton>
                    <ToggleButton
                        variant="secondary"
                        id="tbg-radio-3"
                        value={3}
                    >
                        Top Finishers - Female
                    </ToggleButton>
                </ToggleButtonGroup>
            </Container>
        </Navbar>
    );
}

export default FilterNavbar;
