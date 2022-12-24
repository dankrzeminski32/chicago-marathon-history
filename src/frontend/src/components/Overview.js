import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";
import React from "react";
import { BarMaleFemaleParticipants } from "./graphs/BarMaleFemaleParticipants";
import { LineFinishTimes } from "./graphs/LineFinishTimes";
import { CountryDistribution } from "./graphs/CountryDistribution";

function Overview({ marathon }) {
    return (
        <Container id="selected-container" className="overflow-hidden">
            <Row className="gy-5">
                <Col sm={12} xl={6}>
                    <BarMaleFemaleParticipants marathon={marathon} />
                </Col>
                <Col sm={12} xl={6}>
                    <LineFinishTimes marathon={marathon} />
                </Col>
                <Col sm={12} xl={4}>
                    <CountryDistribution marathon={marathon} />
                </Col>
                <Col sm={12} xl={8}>
                    sm=6
                </Col>
            </Row>
        </Container>
    );
}
export default Overview;
