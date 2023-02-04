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
    const [isSidebarVisibleOnSmallScreen, setSidebarVisibleOnSmallScreen] =
        useState(false);

    useEffect(() => {
        setSelected(1);
    }, [marathon]);

    return (
        <Container fluid className="App fluid">
            <div className="row flex-nowrap">
                <div
                    className={
                        isSidebarVisibleOnSmallScreen
                            ? "col-12"
                            : "d-none d-md-block col-md-2 g-0"
                    }
                >
                    <Sidebar
                        isYearSelected={isYearSelected}
                        onHide={() => {
                            setIsYearSelected(true);
                            setSidebarVisibleOnSmallScreen(false);
                        }}
                        marathonStateChanger={setMarathon}
                        isSidebarVisibleOnSmallScreen={
                            isSidebarVisibleOnSmallScreen
                        }
                    ></Sidebar>
                </div>
                <div
                    className={
                        isSidebarVisibleOnSmallScreen
                            ? "d-none"
                            : "col-12 col-md-10 g-0"
                    }
                >
                    <Header
                        marathon={marathon}
                        isYearSelected={isYearSelected}
                        onShow={() => {
                            setIsYearSelected(false);
                            setMarathon(null);
                            setSidebarVisibleOnSmallScreen(true);
                        }}
                        onGoHome={() => {
                            setIsYearSelected(false);
                            setMarathon(null);
                        }}
                    ></Header>
                    {isYearSelected ? (
                        <FilterNavbar
                            selected={selected}
                            setSelected={setSelected}
                        />
                    ) : null}
                    {isYearSelected ? (
                        <MarathonView marathon={marathon} selected={selected} />
                    ) : null}
                    {isYearSelected ? null : (
                        <Container fluid>{children}</Container>
                    )}
                </div>
            </div>
        </Container>
    );
}
export default Layout;
