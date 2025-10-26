import { useState } from "react";

export default function Select({items}) {

    const [selectedItem, setSelectedItem] = useState(items[0]);

    return (
        <select className="bg-bgColor2 text-text-secondary text-sm rounded-lg outline-none focus:outline-none py-2" value={selectedItem} onChange={(e) => setSelectedItem(e.target.value)}>
            {
                items.map((item) => (
                    <option key={item}>{item}</option>
                ))
            }
        </select>
    )
}