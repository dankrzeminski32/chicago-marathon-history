import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";
import React from "react";
import { useState } from "react";
import { useEffect } from "react";
import Card from "react-bootstrap/Card";
import ListGroup from "react-bootstrap/ListGroup";

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
            {topFinishers.length > 0 && (
                <Row className="h-50">
                    <Col className="topFinisherCard" sm={4}>
                        <Card style={{ width: "18rem" }}>
                            <Card.Header>1st Place</Card.Header>
                            <Card.Img
                                variant="top"
                                src="/defaultathletepic.jpg"
                            />
                            <Card.Body>
                                <Card.Title>
                                    {topFinishers[1].finish_time}
                                </Card.Title>
                            </Card.Body>
                            <ListGroup className="list-group-flush">
                                <ListGroup.Item>
                                    {topFinishers[1]["athlete"].first_name +
                                        " " +
                                        topFinishers[1]["athlete"].last_name}
                                </ListGroup.Item>
                                <ListGroup.Item>
                                    {"Country: " +
                                        topFinishers[1]["athlete"].country}
                                </ListGroup.Item>
                                <ListGroup.Item>
                                    {"Age Group: " + topFinishers[1].age_group}
                                </ListGroup.Item>
                            </ListGroup>
                            <Card.Body>
                                <Card.Link href="#">Card Link</Card.Link>
                            </Card.Body>
                        </Card>{" "}
                    </Col>
                    <Col className="topFinisherCard" sm={4}>
                        <Card style={{ width: "18rem" }}>
                            <Card.Header>1st Place</Card.Header>
                            <Card.Img
                                variant="top"
                                src="/defaultathletepic.jpg"
                            />
                            <Card.Body>
                                <Card.Title>
                                    {topFinishers[0].finish_time}
                                </Card.Title>
                            </Card.Body>
                            <ListGroup className="list-group-flush">
                                <ListGroup.Item>
                                    {topFinishers[0]["athlete"].first_name +
                                        " " +
                                        topFinishers[0]["athlete"].last_name}
                                </ListGroup.Item>
                                <ListGroup.Item>
                                    {"Country: " +
                                        topFinishers[0]["athlete"].country}
                                </ListGroup.Item>
                                <ListGroup.Item>
                                    {"Age Group: " + topFinishers[0].age_group}
                                </ListGroup.Item>
                            </ListGroup>
                            <Card.Body>
                                <Card.Link href="#">Card Link</Card.Link>
                            </Card.Body>
                        </Card>{" "}
                    </Col>
                    <Col className="topFinisherCard" sm={4}>
                        <Card style={{ width: "18rem" }}>
                            <Card.Header>1st Place</Card.Header>
                            <Card.Img
                                variant="top"
                                src="/defaultathletepic.jpg"
                            />
                            <Card.Body>
                                <Card.Title>
                                    {topFinishers[2].finish_time}
                                </Card.Title>
                            </Card.Body>
                            <ListGroup className="list-group-flush">
                                <ListGroup.Item>
                                    {topFinishers[2]["athlete"].first_name +
                                        " " +
                                        topFinishers[2]["athlete"].last_name}
                                </ListGroup.Item>
                                <ListGroup.Item>
                                    {"Country: " +
                                        topFinishers[2]["athlete"].country}
                                </ListGroup.Item>
                                <ListGroup.Item>
                                    {"Age Group: " + topFinishers[2].age_group}
                                </ListGroup.Item>
                            </ListGroup>
                            <Card.Body>
                                <Card.Link href="#">Card Link</Card.Link>
                            </Card.Body>
                        </Card>{" "}
                    </Col>
                </Row>
            )}
        </Container>
    );
}
export default TopFinishers;
