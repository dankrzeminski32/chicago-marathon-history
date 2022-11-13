import { useEffect, useState } from "react";
import { Bar } from "react-chartjs-2";
import { CategoryScale } from "chart.js";
import { Chart, registerables } from "chart.js";

export const BarMaleFemaleParticipants = ({ marathon }) => {
    const [chartData, SetChartData] = useState({});
    const [haveData, setHaveData] = useState(false);

    Chart.register(...registerables);
    console.log(marathon);
    useEffect(() => {
        SetChartData({
            labels: ["Males", "Females"],
            datasets: [
                {
                    label: "Number of Participants",
                    data: [
                        marathon.num_athletes_male,
                        marathon.num_athletes_female,
                    ],
                    backgroundColor: ["#ffbb11", "#ecf0f1"],
                },
            ],
        });
        setHaveData(true);
    }, [marathon]);

    if (!haveData) {
        // here
        return <div>Loading...</div>;
    }
    return (
        <div>
            <Bar data={chartData} />
        </div>
    );
};
