import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";
import React from "react";
import { BarMaleFemaleParticipants } from "./graphs/BarMaleFemaleParticipants";
import { LineFinishTimes } from "./graphs/LineFinishTimes";
import { CountryDistribution } from "./graphs/CountryDistribution";

function Overview({ marathon }) {
    return (
        <Container fluid id="selected-container" className="overflow-hidden">
            <Row>
                <Col sm={12} xl={8}>
                    <BarMaleFemaleParticipants marathon={marathon} />
                </Col>
                <Col sm={12} xl={4}>
                    <CountryDistribution marathon={marathon} />
                </Col>
                <Col sm={12} xl={6}>
                    <LineFinishTimes gender="male" marathon={marathon} />
                </Col>
                <Col sm={12} xl={6}>
                    <LineFinishTimes gender="female" marathon={marathon} />
                </Col>
            </Row>
        </Container>
    );
}
export default Overview;
