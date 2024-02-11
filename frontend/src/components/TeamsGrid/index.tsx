'use client'

import useTeams from '@/hooks/useTeams'
import { Loader, SimpleGrid } from '@mantine/core'
import TeamCard from '../TeamCard'

export default function TeamsGrid() {
  const { isLoading, data } = useTeams()

  if (isLoading) {
    return <Loader color="blue" />
  }
  if (data) {
    return (
      <SimpleGrid cols={3}>
        {data.map((team) => (
          <TeamCard key={team.id} />
        ))}
      </SimpleGrid>
    )
  }

  return <div>Something went wrong</div>
}
