import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";

function MarathonView({ selected }) {
    return (
        <Container id="selected-container">
            <Row className="h-50">
                <Col sm={6}>sm=6 - {selected}</Col>
                <Col sm={6}>sm=6</Col>
            </Row>
            <Row className="h-50">
                <Col sm={6}>sm=6</Col>
                <Col sm={6}>sm=6</Col>
            </Row>
        </Container>
    );
}
export default MarathonView;
