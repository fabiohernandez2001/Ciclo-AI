import { useEffect, useState } from "react";
import Select from "./Select";



  const ALL = ["Ahri","Akali","Ashe","Aatrox","Annie","Anivia","Braum","Brand","Caitlyn","Corki"]
const REGIONS = ["EUW", "NA", "KR", "EUNE", "LAN", "LAS", "OCE", "RU", "TR", "JP"]


function useDebounceValue(value, delay = 300) {
    const [debounce, setDebounce] = useState(value)
    useEffect(() => {
        const id = setTimeout(() => setDebounce(value), delay)
        return () => clearTimeout(id)
    }, [value, delay])
    return debounce
}

export default function Searchbar() {

    const [query, setQuery] = useState("");
    const [suggestions, setSuggestions] = useState([]);
    
    const handleInputChange = async (e) => {
        const inputText = e.target.value
        setQuery(inputText)
        const plainText = inputText.trim().toLowerCase()
        const filteredSuggestions = plainText ? ALL.filter((item) => item.toLowerCase().startsWith(plainText)) : [];
        setSuggestions(filteredSuggestions)
    }

    return (
        <>
            <form className="max-w-lg mx-auto">   
                <label htmlFor="default-search" className="sr-only">Search</label>
                <div className="relative">
                    <div className="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                        <svg className="w-4 h-4 text-text-secondary" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                            <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>
                        </svg>
                    </div>
                    <input 
                        type="search" 
                        id="default-search" 
                        className="block w-full p-4 ps-10 text-sm text-text-primary  rounded-full bg-bgColor2 outline-none focus:outline-none placeholder:text-text-secondary" 
                        placeholder="Search Champions or players" 
                        value={query}
                        onChange={handleInputChange}
                    />
                    
                    <div className="absolute end-4 bottom-2 flex gap-2">
                        <Select items={REGIONS} />
                        <button type="submit" className="text-white bg-secondary hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-2 py-1 ">Search</button>
                    </div>
                    <div className="">
                        { suggestions.length > 0 && (
                            <ul className="absolute w-full flex flex-col bg-bgColor2 mt-1 rounded-lg shadow-lg z-10">
                                {
                                    suggestions.map((suggestion) => (
                                        <li key={suggestion} className="px-4 py-2 hover:bg-bgColor cursor-pointer">{suggestion}</li>
                                    ))
                                }
                            </ul>
                        )}
                    </div>
                </div>
            </form>
        </>
    )
}