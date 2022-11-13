import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";
import React from "react";

function TopFinishers() {
    return (
        <Container id="selected-container">
            <Row className="h-50">
                <Col sm={6}>TOP FINISHERS YAY=6 - </Col>
                <Col sm={6}>sm=6</Col>
            </Row>
            <Row className="h-50">
                <Col sm={6}>sm=6</Col>
                <Col sm={6}>sm=6</Col>
            </Row>
        </Container>
    );
}
export default TopFinishers;
