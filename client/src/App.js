import './App.css';
import React, { useState, useEffect } from "react";

function useRandomizer(){
	const [data, setData] = useState([{}]);
	
	useEffect(() => {
		fetch("/api/random")
		.then(res => res.json())
		.then(data => setData(data))
	}, []);

	return data;
}

function App() {
	const data = useRandomizer();

	return (
		<div className="App">
			<header className="App-header">
				<img src={`${data.image_path}`} alt={`${data.name}`}/>
				<p>{data.name}</p>
				<p>Pokédex ID: {data.pokedexId}</p>
				<p>Types</p>
				<div className="types">
				{
					data.type?.map((type, i) => {
						return <span className={"type " + type.toLowerCase()} key={i}>{type} </span>;
					})
				}
				</div>
			</header>
		</div>
	);
}

export default App;
