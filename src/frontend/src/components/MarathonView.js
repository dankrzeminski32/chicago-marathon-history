import Container from "react-bootstrap/Container";
import React from "react";
import Overview from "./Overview";
import PartipantData from "./ParticipantData";
import TopFinishers from "./TopFinishers";

function MarathonView({ selected, marathon }) {
    switch (selected) {
        case 1:
            return <Overview marathon={marathon}></Overview>;
        case 2:
            return <TopFinishers marathon={marathon}></TopFinishers>;
        case 3:
            return <PartipantData marathon={marathon}></PartipantData>;
        default:
            return <Overview marathon={marathon}></Overview>;
    }
}
export default MarathonView;
