import Container from "react-bootstrap/Container";
import React from "react";
import Overview from "./Overview";
import TopFinishers from "./TopFinishers";

function MarathonView({ selected, marathon }) {
    switch (selected) {
        case 1:
            return <Overview marathon={marathon}></Overview>;
        case 2:
            return (
                <TopFinishers gender="male" marathon={marathon}></TopFinishers>
            );
        case 3:
            return (
                <TopFinishers
                    gender="female"
                    marathon={marathon}
                ></TopFinishers>
            );
        default:
            return <Overview marathon={marathon}></Overview>;
    }
}
export default MarathonView;
