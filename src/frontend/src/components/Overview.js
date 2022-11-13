import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";
import React from "react";
import { BarMaleFemaleParticipants } from "./graphs/BarMaleFemaleParticipants";

function Overview({ marathon }) {
    return (
        <Container id="selected-container">
            <Row className="h-50">
                <Col sm={6}>
                    <BarMaleFemaleParticipants marathon={marathon} />
                </Col>
                <Col sm={6}>sm=6</Col>
            </Row>
            <Row className="h-50">
                <Col sm={6}>sm=6</Col>
                <Col sm={6}>sm=6</Col>
            </Row>
        </Container>
    );
}
export default Overview;
