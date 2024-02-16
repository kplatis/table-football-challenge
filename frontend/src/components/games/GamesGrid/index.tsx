'use client'

import useGames from '@/hooks/useGames'
import {  SimpleGrid } from '@mantine/core'
import GameCard from '../GameCard'
import Loader from '@/components/layout/Loader'

export default function GamesGrid() {
  const { isLoading, data } = useGames()

  if (isLoading) {
    return <Loader />
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
  return null
}
