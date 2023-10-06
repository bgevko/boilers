

const app = document.getElementById("app");

function Header({ title }) {
    return <h1>{title ? title : "Default title"}</h1>;
}

function HomePage() {
    return (
		<div className='
			container h-screen
			flex flex-col
			mx-auto
		'>
			<header className='
				container
				h-20 bg-blue-100
				flex justify-center items-center
			'>
				Header
			</header>

			<section className='
				container
				h-full bg-red-100
				flex
			'>
				<article className='
					container
					flex justify-center items-center
				'>
					Content
				</article>
			</section>
			<footer className='
				container mx-auto
				h-10 bg-green-100
				flex justify-center items-center
			'>
					footer
			</footer>
		</div>
    );
}

ReactDOM.render(<HomePage />, app);
