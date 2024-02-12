'use client'

import useGames from '@/hooks/useGames'
import { Center, Loader, SimpleGrid } from '@mantine/core'
import GameCard from '../GameCard'

export default function GamesGrid() {
  const { isLoading, data } = useGames()

  if (isLoading) {
    return (
      <Center>
        <Loader color="blue" />
      </Center>
    )
  }
  if (data) {
    return (
      <SimpleGrid cols={3}>
        {data.map((game) => (
          <GameCard key={game.id} game={game} />
        ))}
      </SimpleGrid>
    )
  }
  return <div>Something went wrong</div>
}
