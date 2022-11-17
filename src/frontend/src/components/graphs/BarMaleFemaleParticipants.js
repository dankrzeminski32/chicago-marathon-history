import { useEffect, useState } from "react";
import { Bar } from "react-chartjs-2";
import { CategoryScale } from "chart.js";
import { Chart, registerables } from "chart.js";

export const BarMaleFemaleParticipants = ({ marathon }) => {
    const [chartData, SetChartData] = useState({});
    const [chartOptions, SetChartOptions] = useState({});
    const [haveData, setHaveData] = useState(false);

    Chart.register(...registerables);
    console.log(marathon);

    useEffect(() => {
        SetChartData({
            labels: ["Males", "Females"],
            datasets: [
                {
                    data: [
                        marathon.num_athletes_male,
                        marathon.num_athletes_female,
                    ],
                    backgroundColor: ["skyblue", "pink"],
                },
            ],
        });
        setHaveData(true);
    }, [marathon]);

    useEffect(() => {
        SetChartOptions({
            responsive: true,
            plugins: {
                legend: { display: false },
                title: {
                    display: true,
                    text:
                        "Athlete Distribution --- " +
                        marathon.num_athletes +
                        " Total Athletes",
                },
            },
        });
        setHaveData(true);
    }, [marathon]);

    if (!haveData) {
        // here
        return <div>Loading...</div>;
    }
    return (
        <div>
            <Bar options={chartOptions} data={chartData} />
        </div>
    );
};
