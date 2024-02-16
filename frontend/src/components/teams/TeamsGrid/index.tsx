'use client'

import useTeams from '@/hooks/useTeams'
import {  SimpleGrid } from '@mantine/core'
import TeamCard from '../TeamCard'
import Loader from '@/components/layout/Loader'
import MessageWithButton from '@/components/common/MessageWithButton'

export default function TeamsGrid() {
  const { isLoading, data } = useTeams()

  if (isLoading) {
    return <Loader />
  }
  if (data && data.length == 0) {
    return (
      <MessageWithButton
        message="There are no teams created yet"
        buttonMessage="Create a new team"
        buttonUrl="/teams/create"
      />
    )
  }
  if (data) {
    return (
      <SimpleGrid cols={3} className={'mt-8'}>
        {data.map((team) => (
          <TeamCard
            key={team.id}
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
