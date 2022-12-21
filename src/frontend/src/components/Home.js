import Layout from "./Layout";
import { AthleteGrowthByYear } from "./graphs/AthleteGrowthByYear";

function Home() {
    return (
        <Layout>
            <h1>
                Welcome to a brief tour down the history of the Chicago Marathon
            </h1>
            <p>Broken Records, Evolution of the sport, and so much more...</p>
            <AthleteGrowthByYear></AthleteGrowthByYear>
        </Layout>
    );
}
export default Home;
