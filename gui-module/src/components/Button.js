const Button = ({text, color, onClick}) => {
    return(
        <button className='button'
        style={{background:color}}
        data-testid="button"
        onClick={onClick}>
            {text}
        </button>
    )
}

export default Button