import { use, useEffect, useId, useMemo, useRef, useState } from "react";
import Select from "./Select";
import useDebounceValue from "../../hooks/useDebounceValue";
import useOnClickOutside from "../../hooks/useOnClickOutside";
import { useQuery } from "@tanstack/react-query";
import { fetchChampion } from "../../utils/http";

const CHAMPIONS_DUMMY = ["Ahri","Akali","Ashe","Aatrox","Annie","Anivia","Braum","Brand","Caitlyn","Corki"]
const REGIONS = ["EUW", "NA", "KR", "EUNE", "LAN", "LAS", "OCE", "RU", "TR", "JP"]

export default function Searchbar() {

    const [query, setQuery] = useState("");
    const [open, setOpen] = useState(false);
    const debouncedQuery = useDebounceValue(query, 300)
    const [highlighted, setHighlighted] = useState(-1)

    const inputId = useId()
    const listboxId = `${inputId}-suggestions`
    const optionId = (i) => `${listboxId}-opt-${i}`

    const inputRef = useRef(null)
    const listRef = useRef(null)
    const containerRef = useRef(null)

    const { data: champions, isLoading, error } = useQuery({
        queryKey: ['champions'],
        queryFn: ({signal}) => fetchChampion({signal }),
    })

    let championsList = CHAMPIONS_DUMMY

    if ( champions ) {
        console.log(champions)
    }


    const suggestions = useMemo(() => {
        const plainText = debouncedQuery.trim().toLowerCase()
        if (!plainText) {
            return []
        }
        setOpen(true)
        return CHAMPIONS_DUMMY.filter((champion) =>
            champion.toLowerCase().startsWith(plainText)
        );
    }, [debouncedQuery]);

    useOnClickOutside(containerRef, () => setOpen(false))
    
    const handleInputChange = async (e) => {
        setQuery(e.target.value)
    }

    const handleSubmit = (event) => {
        event.preventDefault()
        const trimmedQuery = query.trim()
        if (!trimmedQuery) {
            return
        }
        onSubmit?.(trimmedQuery)
    }

    const handleSuggestionClick = (suggestion) => {
        setQuery(suggestion)
    }


    return (
        <>
            <form className="max-w-lg mx-auto" onSubmit={handleSubmit} autoComplete="off">   
                <label htmlFor={inputId} className="sr-only">Search</label>
                <div className="relative" ref={containerRef}>
                    <div className="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                        <svg className="w-4 h-4 text-text-secondary" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                            <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>
                        </svg>
                    </div>
                    <input 
                        ref={inputRef}
                        type="search" 
                        id={inputId} 
                        className="block w-full p-4 ps-10 text-sm text-text-primary  rounded-full bg-bgColor2 outline-none focus:outline-none placeholder:text-text-secondary" 
                        placeholder="Search Champions or players" 
                        value={query}
                        onChange={handleInputChange}
                        //onKeyDown={handleKeyDown}
                        role="combobox"
                        aria-autocomplete="list"
                        aria-expanded={open}
                        aria-controls={open ? listboxId : undefined}
                    />
                    <div className="absolute end-4 bottom-2 flex gap-2">
                        <Select items={REGIONS} />
                        <button type="submit" className="text-white bg-secondary hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-2 py-1 ">Search</button>
                    </div>
                    <div className="">
                        { open && (
                            <ul 
                                ref={listRef}
                                id={listboxId}
                                role="listbox"
                                className="absolute w-full flex flex-col bg-bgColor2 mt-1 rounded-lg shadow-lg z-10">
                                {
                                    suggestions.map((suggestion, index) => {
                                        const active = index === highlighted
                                        return(
                                            <li 
                                                id={optionId(index)}
                                                key={suggestion} 
                                                role="option"
                                                tabIndex={-1}
                                                aria-selected={active}
                                                onMouseDown={(event) => event.preventDefault()}
                                                onClick={() => handleSuggestionClick(suggestion)}
                                                className="px-4 py-2 hover:bg-secondary/10 cursor-pointer"
                                            >
                                                {suggestion}
                                            </li>
                                        )
                                    })
                                }
                            </ul>
                        )}
                    </div>
                </div>
            </form>
        </>
    )
}