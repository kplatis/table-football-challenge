'use client'

import useTeams from '@/hooks/useTeams'
import { Center, Loader, SimpleGrid } from '@mantine/core'
import TeamCard from '../TeamCard'

export default function TeamsGrid() {
  const { isLoading, data } = useTeams()
  if (isLoading) {
    return (
      <Center>
        <Loader color="blue" />
      </Center>
    )
  }
  if (data) {
    return (
      <SimpleGrid cols={3} className={'mt-8'}>
        {data.map((team) => (
          <TeamCard
            key={team.id}
            id={team.id}
            name={team.name}
            firstPlayer={team.first_player}
            secondPlayer={team.second_player}
          />
        ))}
      </SimpleGrid>
    )
  }

  return <div>Something went wrong</div>
}
