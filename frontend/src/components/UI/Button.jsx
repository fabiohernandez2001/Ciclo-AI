export default function Button({ children, onClick, type = "button", ...props }) {
    return (
        <button
            type={type}
            onClick={onClick}
            className="px-4 py-2 bg-bgColor text-text-primary rounded hover:bg-primary-dark"
            {...props}
        >
            {children}
        </button>
    )
}