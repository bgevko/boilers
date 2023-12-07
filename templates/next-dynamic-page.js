// Next dynamic page example

// export const revalidate = 86400

// Get static parameters
export async function generateStaticParams() {
	// Implement some fetch logic here, for example:

	// try {
	// 	const posts = await getPostsMeta('projects')
	// 	if (!posts) return []
	// 	return posts.map(post => ({ postId: post.id }))
	// } catch (err) {
	// 	console.log("generateStaticParams:error: ", err)
	// 	return []
	// }
}

// Generate metadata
export async function generateMetadata({ params }) {
	// try {
	// 	const post = await getPostBySlug(params.slug, 'projects')
	// 	if (!post) return { title: 'Post not found' }
	//
	// 	return {
	// 		title: post.meta.title,
	// 		description: post.meta.description,
	// 	}
	// } catch (err) {
	// 	console.error("generateMetadata:error: ", err)
	// 	return { title: 'Something went wrong.' }
	// }
}

export default function DynamicPage({ params }) {
	// Use params here, for example:
	// const post = await getPostBySlug(params.slug, 'projects')
	// if (!post) return notFound()
	// const { meta, content } = post
	//  return (
	//    <main className="pt-4 pb-20 flex w-full flex flex-col items-center lg:pb-24">
	// 		<Article meta={meta} content={content} />
	// 	</main>
	// )
}
