import Header from "./Header";
import Sidebar from "./Sidebar";
import Container from "react-bootstrap/Container";
import { useState } from "react";
import FilterNavbar from "./FilterNavbar";
import MarathonView from "./MarathonView";
import { useLocation } from "react-router-dom";
import { useEffect } from "react";

function Layout({ children }) {
    const [isYearSelected, setIsYearSelected] = useState(false);
    const [marathon, setMarathon] = useState(null);
    const [selected, setSelected] = useState(1);

    useEffect(() => {
        setSelected(1);
    }, [marathon]);

    return (
        <div className="App">
            <Sidebar
                isYearSelected={isYearSelected}
                onHide={() => {
                    setIsYearSelected(true);
                }}
                marathonStateChanger={setMarathon}
            ></Sidebar>
            <Header
                marathon={marathon}
                isYearSelected={isYearSelected}
                onShow={() => {
                    setIsYearSelected(false);
                    setMarathon(null);
                }}
            ></Header>
            {isYearSelected ? (
                <FilterNavbar selected={selected} setSelected={setSelected} />
            ) : null}
            {isYearSelected ? (
                <MarathonView marathon={marathon} selected={selected} />
            ) : null}
            {isYearSelected ? null : <Container>{children}</Container>}
        </div>
    );
}
export default Layout;
