import Layout from "./Layout";
import { useLocation } from "react-router-dom";

function MarathonView(props) {
    const location = useLocation();
    console.log(props, " props");
    console.log(location, " useLocation Hook");
    const marathon = location.state?.marathon;

    return (
        <Layout>
            <h1>{marathon.year}</h1>
        </Layout>
    );
}
export default MarathonView;
