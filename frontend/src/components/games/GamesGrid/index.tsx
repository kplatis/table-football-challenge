'use client'

import useGames from '@/hooks/useGames'
import { SimpleGrid } from '@mantine/core'
import GameCard from '../GameCard'
import Loader from '@/components/layout/Loader'
import MessageWithButton from '@/components/common/MessageWithButton'

export default function GamesGrid() {
  const { isLoading, data } = useGames()

  if (isLoading) {
    return <Loader />
  }
  if (data && data.length == 0) {
    return (
      <MessageWithButton
        message="There are no games created yet"
        buttonMessage="Create a new game"
        buttonUrl="/games/create"
      />
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

  return null
}
