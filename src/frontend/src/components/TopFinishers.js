import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";
import React from "react";
import { useState } from "react";
import { useEffect } from "react";

function TopFinishers({ marathon, gender }) {
    const [error, setError] = useState(null);
    const [topFinishers, setTopFinishers] = useState([]);

    //if gender=="male" or gender=="female"

    const fetchData = async (genderID) => {
        const response = await fetch(
            "http://127.0.0.1:5000/api/results/" +
                marathon.year +
                "/" +
                genderID +
                "/3"
        );

        const data = await response.json();

        setTopFinishers(data);
    };
    useEffect(() => {
        var genderID = "M";
        if (gender === "male") {
            genderID = "M";
        } else {
            genderID = "F";
        }
        fetchData(genderID);
    }, [marathon, gender]);

    return (
        <Container id="selected-container">
            <Row className="h-50">
                {topFinishers.length > 0 &&
                    topFinishers.map((finisher) => (
                        <Col sm={4}>{finisher.finish_time}</Col>
                    ))}
            </Row>
        </Container>
    );
}
export default TopFinishers;
